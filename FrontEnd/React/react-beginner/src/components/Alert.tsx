import { ReactNode } from "react";

interface AlertProps {
    children: ReactNode;
    alertType:
        | "primary"
        | "secondary"
        | "success"
        | "danger"
        | "warning"
        | "info"
        | "light"
        | "dark";
    onClose: () => void;
}

export default function Alert({ children, alertType, onClose }: AlertProps) {
    return (
        <div
            className={"alert alert-" + alertType + " alert-dismissible"}
            role="alert"
        >
            {children}
            <button
                type="button"
                className="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
                onClick={onClose}
            ></button>
        </div>
    );
}
