import React, { useState } from "react";

type Props = {
  onAddTodo: (title: string) => void;
};

const AddTodo: React.FC<Props> = props => {
  const [newTitle, setNewTitle] = useState("");
  return (
    <form
      onSubmit={event => {
        event.preventDefault();
        props.onAddTodo(newTitle);
        setNewTitle("");
      }}
    >
      <input
        value={newTitle}
        onChange={event => setNewTitle(event.target.value)}
      />
      <button disabled={newTitle.length === 0}>add</button>
    </form>
  );
};

export default AddTodo;
