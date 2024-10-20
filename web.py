import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["New_Todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("My To-do App")
st.write("I am Here to improve your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a Todo...."
              , on_change=add_todo, key="New_Todo")
