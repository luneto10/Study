import { useState } from "react";
import "./App.css";
import { v4 as uuidv4 } from "uuid";
import TodoList from "./components/TodoList";

function App() {
    const [todos, setTodos] = useState([
        {
            id: uuidv4(),
            todo: "Buy butter",
            completed: false,
        },
        { id: uuidv4(), todo: "Buy eggs", completed: false },
        { id: uuidv4(), todo: "Buy bread", completed: false },
        { id: uuidv4(), todo: "Buy cheese", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
        { id: uuidv4(), todo: "Buy milk", completed: false },
    ]);

    const handleToggle = (id: string) => {
        setTodos((prevTodos) =>
            prevTodos.map((todo) =>
                todo.id === id ? { ...todo, completed: !todo.completed } : todo
            )
        );
    };

    const handleDelete = (id: string) => {
        setTodos((prevTodos) => prevTodos.filter((todo) => todo.id !== id));
    };

    const handleAdd = (todoText: string) => {
        setTodos((prevTodos) => [
            ...prevTodos,
            { id: uuidv4(), todo: todoText, completed: false },
        ]);
    };

    const handleDeleteAll = () => {
        console.log("Delete all");
        setTodos([]);
    };

    return (
        <div className="d-flex flex-column justify-content-center align-items-center vh-100">
            <TodoList
                todos={todos}
                handleToggle={handleToggle}
                handleDelete={handleDelete}
                handleAdd={handleAdd}
                handleDeleteAll={handleDeleteAll}
            />
        </div>
    );
}

export default App;