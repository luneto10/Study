import { useState } from "react";
import { Modal, Button, Form } from "react-bootstrap";

interface AddTodoModalProps {
    show: boolean;
    handleClose: () => void;
    handleAdd: (todoText: string) => void;
}

export default function AddItem({
    show,
    handleClose,
    handleAdd,
}: AddTodoModalProps) {
    const [todoText, setTodoText] = useState("");

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        handleAdd(todoText);
        setTodoText("");
        handleClose();
    };

    return (
        <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>Add New Todo</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form onSubmit={handleSubmit}>
                    <Form.Group controlId="formTodoText">
                        <Form.Label>What do you want to do?</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder="Enter todo"
                            value={todoText}
                            onChange={(e) => setTodoText(e.target.value)}
                            required
                        />
                    </Form.Group>
                    <Button variant="primary" type="submit" className="mt-3">
                        Add Todo
                    </Button>
                </Form>
            </Modal.Body>
        </Modal>
    );
}
