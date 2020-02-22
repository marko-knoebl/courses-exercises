import React from "react";

import "./TodoApp.css";
import useTodos from "./useTodos";
import AddTodo from "./AddTodo";
import TodoList from "./TodoList";
import LoadFromApi from "./LoadFromApi";
import Stats from "./Stats";

const TodoApp: React.FC = () => {
  const { todos, addTodo, toggleTodo, loadFromApi, isLoading } = useTodos();
  return (
    <div className="TodoApp">
      <h1>Todo</h1>
      <Stats todos={todos} />
      <LoadFromApi isLoading={isLoading} onLoad={loadFromApi} />
      <TodoList todos={todos} onToggle={toggleTodo} />
      <AddTodo onAddTodo={addTodo} />
    </div>
  );
};

export default TodoApp;
