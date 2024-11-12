import { useState } from "react";

//{ items: string[], heading: string }
interface ListGroupProps {
    items: string[];
    heading: string;
    onSelectItem: (item: string) => void;
}

function ListGroup({ items, heading, onSelectItem }: ListGroupProps) {
    const message = items.length === 0 ? <p>There are no items</p> : null;
    const getMessage = () => {
        if (items.length === 0) {
            return <p>There are no items</p>;
        }
        return null;
    };

    // Hook
    const [selectIndex, setSelectIndex] = useState(-1);

    // event handler
    const handleClick = (event: React.MouseEvent) => {
        console.log(event);
    };

    return (
        <>
            <h1>{heading}</h1>
            {items.length === 0 && <p>There are no items</p>}
            <ul className="list-group">
                {items.map((item, index) => (
                    <li
                        key={item}
                        className={
                            selectIndex === index
                                ? "list-group-item active"
                                : "list-group-item"
                        }
                        onClick={() => {
                            setSelectIndex(index);
                            onSelectItem(item);
                        }}
                    >
                        {item}
                    </li>
                ))}
            </ul>
        </>
    );
}

export default ListGroup;
