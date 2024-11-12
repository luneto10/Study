import DeleteOutlineIcon from "@mui/icons-material/DeleteOutline";
import styles from "../styles/TodoItem.module.css";
import { Todo } from "../types/types";


interface TodoItemProps extends Todo {
    handleToggle: (id: string) => void;
    handleDelete: (id: string) => void;
}

export default function TodoItem({
    id,
    todo,
    completed,
    handleToggle,
    handleDelete,
}: TodoItemProps) {
    return (
        <li
            className={`d-flex align-items-center justify-content-between ${styles["item-box"]} p-2 rounded-2`}
        >
            <div className="d-flex align-items-center">
                <input
                    className="form-check-input me-2"
                    type="checkbox"
                    id={`todo-${id}`}
                    checked={completed}
                    onChange={() => handleToggle(id)}
                />
                <label className="form-check-label" htmlFor={`todo-${id}`}>
                    {completed ? <del>{todo}</del> : todo}
                </label>
            </div>
            <button
                className={"btn border-0 " + styles["hover-glow"]}
                onClick={() => handleDelete(id)}
            >
                <DeleteOutlineIcon className="hover-glow" />
            </button>
        </li>
    );
}
