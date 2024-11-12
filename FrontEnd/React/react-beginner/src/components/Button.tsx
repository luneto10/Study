import React from "react";

interface ButtonProps {
    children: React.ReactNode;
    color?: 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'info' | 'light' | 'dark';
    onClick?: () => void;
}

export default function Button({ children, color = "primary", onClick }: ButtonProps) {
    return (
        <button className={"btn btn-" + color} onClick={onClick}>
            {children}
        </button>
    );
}
