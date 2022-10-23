import streamlit as st

#session_state.~ is global

def main():
    st.title("Counter")

    if "count" not in st.session_state: #初期値の設定
        st.session_state.count = 0

    increment = st.button("Add")        #ボタンの配置,押されたらincrementがTrue
    if increment:
        st.session_state.count += 1

    def delete():                       #Delete関数の定義
        st.session_state.count -= 1
    
    st.button("del",on_click = delete)  #Deleteが押されると(on_click)deleteの関数を実行

    if st.button("Clear") == True:      #条件式(ボタンの配置,押されたらClearがTrue == True)
        st.session_state.count = 0
    
    st.text_input("Message",key = "text_input")

    def change_value():
        st.session_state["text_input"] = str(st.session_state.count)

    st.button("Show",on_click = change_value)

    st.write("Count = ", st.session_state.count)


if __name__ == "__main__":
    main()