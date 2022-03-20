import Webcam from "react-webcam";
import { useEffect, useState, useRef, useCallback } from "react";

const videoConstraints = {
    width: 720,
    height: 360,
    facingMode: "user"
};

const Test = () => {
    const [isCaptureEnable, setCaptureEnable] = useState(false);
    const webcamRef = useRef(null);
    const [url, setUrl] = useState(null);
    const capture = useCallback(() => {
        const imageSrc = webcamRef.current?.getScreenshot();
        if (imageSrc) {
            setUrl(imageSrc);
        }
    }, [webcamRef]);

    return (
        <div>
            <header>
                <h1>camera app</h1>
            </header>
            {isCaptureEnable || (
                <button onClick={() => setCaptureEnable(true)}>Start</button>
            )}
            {isCaptureEnable && (
                <>
                    <div>
                        <button onClick={() => setCaptureEnable(false)}>End</button>
                    </div>
                    <div>
                        <Webcam
                            audio={false}
                            width={540}
                            height={360}
                            ref={webcamRef}
                            screenshotFormat="image/jpeg"
                            videoConstraints={videoConstraints}
                        />
                    </div>
                    <button onClick={capture}>capture</button>
                </>
            )}
            {url && (
                <>
                    <div>
                        <button
                            onClick={() => {
                                setUrl(null);
                            }}
                        >
                            delete
                        </button>
                    </div>
                    <div>
                        <img src={url} alt="Screenshot" />
                    </div>
                </>
            )}
        </div>
    );
};

export default Test;