import Webcam from "react-webcam";
import { useEffect, useState, useRef, useCallback } from "react";

const videoConstraints = {
    width: 720,
    height: 360,
    facingMode: "user"
};

const Test = ({childToParent}) => {
    const webcamRef = useRef(null);
    const mediaRecorderRef = useRef(null);
    const [capturing, setCapturing] = useState(false);
    const [recordedChunks, setRecordedChunks] = useState([]);
    

    const handleStartCaptureClick = useCallback(() => {
        setCapturing(true);
        mediaRecorderRef.current = new MediaRecorder(webcamRef.current.stream, {
            mimeType: "video/webm"
        });
        mediaRecorderRef.current.addEventListener(
            "dataavailable",
            handleDataAvailable
        );
        mediaRecorderRef.current.start();
    }, [webcamRef, setCapturing, mediaRecorderRef]);

    const handleDataAvailable = useCallback(
        ({ data }) => {
            if (data.size > 0) {
                setRecordedChunks((prev) => prev.concat(data));
            }
        },
        [setRecordedChunks]
    );

    const handleStopCaptureClick = useCallback(() => {
        mediaRecorderRef.current.stop();
        setCapturing(false);
    }, [mediaRecorderRef, webcamRef, setCapturing]);

    const handleDownload = useCallback(() => {
        if (recordedChunks.length) {
            const blob = new Blob(recordedChunks, {
                type: "video/webm"
            });
            var fileOfBlob = new File([blob], 'videoRecording.mp4');
            childToParent(fileOfBlob);
            setRecordedChunks([]);
        }
    }, [recordedChunks]);


    return (
        <>
            <Webcam audio={false} ref={webcamRef} />
            {capturing ? (
                <button className="flex-1 btn bg-red-400 hover:bg-red-500 border-none" onClick={handleStopCaptureClick}>Stop Capture</button>
            ) : (
                <button className="flex-1 btn bg-red-400 hover:bg-red-500 border-none" onClick={handleStartCaptureClick}>Start Capture</button>
            )}
            {recordedChunks.length > 0 && (
                <button className="flex-1 btn bg-red-400 hover:bg-red-500 border-none" onClick={handleDownload}>Upload</button>
            )}
        </>
    );
};

export default Test;