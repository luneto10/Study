import TodoItem from "./TodoItem";
import { Todo } from "../types/types";
import styles from "../styles/TodoList.module.css";
import { useState } from "react";
import AddItem from "./AddItem";
import AddCircleOutlineSharpIcon from "@mui/icons-material/AddCircleOutlineSharp";
import DeleteAll from "./DeleteAll";
import { Button } from "react-bootstrap";
import SimpleBar from "simplebar-react";
import "simplebar-react/dist/simplebar.min.css";
import "../styles/CustomScrollBar.css";

interface TodoListProps {
    todos: Todo[];
    handleToggle: (id: string) => void;
    handleDelete: (id: string) => void;
    handleDeleteAll: () => void;
    handleAdd: (todoText: string) => void;
}

export default function TodoList({
    todos,
    handleToggle,
    handleDelete,
    handleAdd,
    handleDeleteAll,
}: TodoListProps) {
    const [showItemModal, setShowModal] = useState(false);
    const openItemModal = () => setShowModal(true);
    const closeItemModal = () => setShowModal(false);

    const [showConfirmDeleteModal, setShowConfirmDeleteModal] = useState(false);

    const openConfirmDeleteModal = () => setShowConfirmDeleteModal(true);
    const closeConfirmDeleteModal = () => setShowConfirmDeleteModal(false);

    return (
        <div
            className="d-flex flex-column justify-content-center align-items-center"
            style={{ maxHeight: "95vh" }}
        >
            <div className="d-flex justify-content-between align-items-center w-100 p-3 border-bottom border-dark">
                <p className="h1">Todo List</p>

                <div>
                    <button
                        className={"btn border-0 " + styles["hover-glow"]}
                        onClick={openItemModal}
                    >
                        <AddCircleOutlineSharpIcon />
                    </button>
                    <Button
                        variant="outline-danger"
                        size="sm"
                        onClick={openConfirmDeleteModal}
                    >
                        Delete All
                    </Button>
                </div>
            </div>

            <SimpleBar style={{ maxHeight: "70vh", margin: "0 1rem" }}>
                <div className={`${styles["itemList"]}`}>
                    {todos.length === 0 ? (
                        <p className="text-center m-0 border-top">
                            No todos yet! Click the + button to add one
                        </p>
                    ) : (
                        <ul className="list-group border-top">
                            {todos.map((todo) => (
                                <TodoItem
                                    key={todo.id}
                                    {...todo}
                                    handleToggle={handleToggle}
                                    handleDelete={handleDelete}
                                />
                            ))}
                        </ul>
                    )}
                </div>
            </SimpleBar>

            <AddItem
                show={showItemModal}
                handleClose={closeItemModal}
                handleAdd={handleAdd}
            />

            <DeleteAll
                show={showConfirmDeleteModal}
                handleClose={closeConfirmDeleteModal}
                handleDeleteAll={handleDeleteAll}
            />
        </div>
    );
}