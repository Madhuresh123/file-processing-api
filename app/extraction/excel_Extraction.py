import pandas as pd
from .Base_Extraction import BaseExtraction

class ExcelExtraction(BaseExtraction):

    def extract(self, file_path: str) -> str:
        try:
            sheets = pd.read_excel(
                file_path,
                sheet_name=None,
                engine="openpyxl"
            )

            text = []

            for sheet_name, df in sheets.items():
                text.append(f"--- Sheet: {sheet_name} ---")
                text.append(
                    df.fillna("")
                      .astype(str)
                      .to_string(index=False)
                )

            return "\n".join(text)

        except Exception as e:
            # IMPORTANT: propagate meaningful error
            raise RuntimeError(f"Excel extraction failed: {str(e)}")
