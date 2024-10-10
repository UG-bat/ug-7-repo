import streamlit as st
from onegai import onegai, kitekure  # onegaiディレクトリからモジュールをインポート

# ページ初期設定
def init_page():
    st.set_page_config(
        page_title="Ask about PDF(s)",
        page_icon="📄"
    )

# アプリのメインロジック
def main():
    init_page()

    st.sidebar.title("Navigation")  # サイドバーにタイトルを設定
    page = st.sidebar.selectbox("Select a page", ["Home", "Upload PDF", "PDF QA"])  # ページ選択

    # 各ページの表示
    if page == "Home":
        st.title("Home Page")
        st.write("This is the home page.")
    elif page == "Upload PDF":
        onegai.show()  # onegai.pyの中のshow関数を呼び出す
    elif page == "PDF QA":
        kitekure.show()  # kitekure.pyの中のshow関数を呼び出す

def main():
    init_page()

    st.sidebar.success("上のメニューから選択してください。")

    st.markdown(
    """
    ### Ask about PDF(s) 

    - このアプリでは、アップロードしたPDFについての質問をすることができます。
    - まずは左のメニューから `upload_pdf` を選択してPDFをアップロードしてください。
    - PDFをアップロードしたら `pdf_QA` を選択して質問をしてみましょう。
    """
    )


# メイン関数の実行
if __name__ == '__main__':
    main()

