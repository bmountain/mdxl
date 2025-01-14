import re
from pathlib import Path

import pandas as pd

from src.config_loader import Config


class MarkdownTestParser:

    def __init__(self, markdown_content: str, config: Config):
        """Markdownテスト仕様書を解析し、データフレームに変換するクラス

        Args:
            markdown_content (str):  Markdown形式のテスト仕様書
            config (Config):         設定情報


        """

        self.markdown_content = markdown_content
        self.config = config

        # e.g.) ["大項目", "中項目", "小項目", "No.", "正常／異常", "テスト結果", "確認手順", "期待値", "備考"]
        self.columns = self.config.columns.model_fields.keys()
        print('self.columns', self.columns)
        self.data = []

        self.pattern_section = re.compile(self.config.columns.section.md_pattern, re.MULTILINE)
        self.pattern_subsection = re.compile(self.config.columns.subsection.md_pattern, re.MULTILINE)
        self.pattern_testcase = re.compile(self.config.columns.testcase.md_pattern, re.MULTILINE)
        self.pattern_step = re.compile(self.config.columns.step.md_pattern, re.MULTILINE)
        self.pattern_expectation = re.compile(self.config.columns.expectation.md_pattern, re.MULTILINE)
        self.pattern_note = re.compile(self.config.columns.notes.md_pattern, re.MULTILINE)
        self.pattern_bikou = re.compile(self.config.columns.bikou.md_pattern, re.MULTILINE)

    def parse(self) -> pd.DataFrame:
        """Markdownファイルを解析し、データフレーム用のデータを作成します。

        Returns:
            pd.DataFrame: 解析結果のデータフレーム

        Notes:
            - テスト仕様書のデフォルト形式は以下の通り
                # 大項目
                ## 中項目
                ### 小項目
                #### [正常|異常] [OK|NG|--] テストケース名
                1. 確認手順
                2. 確認手順
                * [ ] 期待値
                - 備考
        """
        current_section = None
        current_subsection = None

        lines = self.markdown_content.split('\n')

        for i, line in enumerate(lines):
            section_match = self.pattern_section.match(line)
            subsection_match = self.pattern_subsection.match(line)
            testcase_match = self.pattern_testcase.match(line)

            if section_match:
                current_section = section_match.group(1)
                current_subsection = None  # Reset subsection when a new section is found
            elif subsection_match:
                current_subsection = subsection_match.group(1)
            elif testcase_match:
                steps, expectations, notes = [], [], []
                test_case_type, test_result, test_case_name = \
                    testcase_match.group(1), testcase_match.group(2) , testcase_match.group(3)
                steps, expectations, notes, conduction_date, conductor, check_date, checker, bikou = [], [], [], None, None, None, None, []

                for subline in lines[i + 1:]:
                    step_match = self.pattern_step.match(subline)
                    expectation_match = self.pattern_expectation.match(subline)
                    note_match = self.pattern_note.match(subline)
                    bikou_match = self.pattern_bikou.match(subline)

                    if step_match:
                        steps.append(step_match.group(1))
                    elif expectation_match:
                        expectations.append(expectation_match.group(1))
                    elif note_match:
                        notes.append(note_match.group(1))
                    elif bikou_match:
                        bikou.append(bikou_match.group(1))
                    elif subline.startswith('####') or subline.startswith('###') or subline.startswith('##'):
                        break

                # データフレーム用の行データ作成
                self.data.append([
                    len(self.data) + 1,
                    current_section,
                    current_subsection,
                    test_case_name,
                    test_case_type,
                    '\n'.join([f"{note}" for note in notes]),
                    '\n'.join([f"{step}" for i, step in enumerate(steps)]),
                    '\n'.join([f"{expectation}" for expectation in expectations]),
                    conduction_date,
                    conductor,
                    test_result,
                    check_date,
                    checker,
                    '\n'.join([f"{bikou_el}" for bikou_el in bikou]),
                ])

        df = pd.DataFrame(self.data, columns=self.columns)
        print(df[df['bikou'].notna()].head())
        return pd.DataFrame(self.data, columns=self.columns)


def read_markdown_file(file_path: Path) -> str:
    print(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Markdownファイルが見つかりません: {file_path}")
    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.read()
