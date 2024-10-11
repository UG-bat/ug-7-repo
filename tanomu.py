import streamlit as st
from onegai.onegai import show as onegai_show  # onegaiディレクトリからモジュールをインポート
from onegai.kitekure import show as kitekure_show

# ページ初期設定
def init_page():
    st.set_page_config(
        page_title="Ask about PDF(s)",
        page_icon="📄"
    )

# PDFのアップロード処理
def upload_pdf():
    st.title("Upload PDF")
    uploaded_file = st.file_uploader("PDFファイルをアップロードしてください", type="pdf")
    
    if uploaded_file is not None:
        st.write("PDFファイルがアップロードされました。")
        pdf_text = ""
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                pdf_text += page.get_text()

        # PDFの内容を確認
        st.text_area("PDFの内容", pdf_text[:5000])  # 5000文字まで表示

        # セッションにPDFのテキストを保存
        st.session_state['pdf_text'] = pdf_text
        st.success("PDFのテキストが保存されました。")


def main():
    init_page()
    
    st.sidebar.title("Navigation")  # サイドバーにタイトルを設定
    page = st.sidebar.selectbox("Select a page", ["Home", "Upload PDF", "PDF QA"])  # ページ選択

    # 各ページの表示
    if page == "Home":
        st.title("Home Page")
        st.write("This is the home page.")
    elif page == "Upload PDF":
        onegai_show()  # onegai.pyの中のshow関数を呼び出す
    elif page == "PDF QA":
        kitekure_show()  # kitekure.pyの中のshow関数を呼び出す

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

