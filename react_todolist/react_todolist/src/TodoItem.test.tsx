import React from "react";
import { render } from "@testing-library/react";
import TodoItem from "./TodoItem";

it("renders a todo with a given title", () => {
  const title = "test-title";
  const instance = render(
    <TodoItem
      title={title}
      completed={false}
      onToggle={() => {}}
      onDelete={() => {}}
    />
  );
  const todoElement = instance.getByText(new RegExp(title));
  expect(todoElement).toBeInTheDocument();
});

it("renders a completed todo", () => {
  const title = "test-title";
  const instance = render(
    <TodoItem
      title={title}
      completed={true}
      onToggle={() => {}}
      onDelete={() => {}}
    />
  );
  const todoElement = instance.getByText(new RegExp(title));
  expect(todoElement.className).toEqual("todo-item-text-completed");
});
