import React from "react";

import "./TodoItem.css";

type Props = {
  title: string;
  completed: boolean;
  onToggle: () => void;
};

const TodoItem: React.FC<Props> = props => {
  let className = "TodoItem";
  if (props.completed) {
    className += " completed";
  }
  return (
    <li onClick={props.onToggle} className={className}>
      {props.completed ? "DONE" : "TODO"}: {props.title}
    </li>
  );
};

export default TodoItem;
