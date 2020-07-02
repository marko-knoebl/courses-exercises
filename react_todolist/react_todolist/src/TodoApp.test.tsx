import React from "react";
import { render, fireEvent } from "@testing-library/react";
import TodoApp from "./TodoApp";

it("renders a todo app", () => {
  const instance = render(<TodoApp />);
});

describe("interactions", () => {
  const createTodoAppWithOneTodo = () => {
    const instance = render(<TodoApp />);
    const newTitleInput = instance.getByLabelText(
      /new title:/i
    ) as HTMLInputElement;
    fireEvent.change(newTitleInput, { target: { value: "first todo" } });
    fireEvent.click(instance.getByText("add"));
    return instance;
  };

  it("creates a todo app with one todo", () => {
    const instance = createTodoAppWithOneTodo();
    const todoElements = instance.getAllByText(/TODO/);
    expect(todoElements).toHaveLength(1);
  });

  it("lets a user toggle a todo", () => {
    // arrange
    const instance = createTodoAppWithOneTodo();
    // act
    fireEvent.click(instance.getByText(/TODO/));
    // assert
    expect(instance.getByText(/DONE/)).toBeInTheDocument();
  });

  it("lets a user delete a todo", () => {
    const instance = createTodoAppWithOneTodo();
    fireEvent.click(instance.getByText("X"));
    expect(instance.queryAllByText(/DONE/)).toHaveLength(0);
    expect(instance.queryAllByText(/TODO/)).toHaveLength(0);
  });
});

it("fetches todos from an API", async () => {
  // arrange
  const fetch = globalThis.fetch;
  globalThis.fetch = () =>
    Promise.resolve({
      json: () =>
        Promise.resolve([
          { id: 1, title: "one", completed: false },
          { id: 2, title: "two", completed: true },
        ]),
    }) as Promise<Response>;
  const instance = render(<TodoApp />);

  // act
  fireEvent.click(instance.getByText(/load from API/));

  // assert
  const allTodos = await instance.findAllByText(/(TODO)|(DONE)/);
  const numTodos = allTodos.length;
  expect(numTodos).toBeGreaterThanOrEqual(2);

  // cleanup
  globalThis.fetch = fetch;
});
