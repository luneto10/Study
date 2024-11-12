import { useState } from "react";
import Alert from "./components/Alert";
import Button from "./components/Button";

function App() {
    const [alertVisible, setAlertVisible] = useState(false);

    return (
        <div>
            {alertVisible && (
                <Alert
                    alertType="warning"
                    onClose={() => setAlertVisible(false)}
                >
                    Kamilla EH MUITO LINDA NE HEHEHEEH LINDONA CASA COMIGO EU TE AMI MUITO
                </Alert>
            )}
            <div className="container d-flex justify-content-center align-items-center vh-100">
                <Button color="primary" onClick={() => setAlertVisible(true)}>
                    Click Me
                </Button>
            </div>
        </div>
    );
}

export default App;
