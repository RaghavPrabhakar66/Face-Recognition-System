import Webcam from "react-webcam";
import { useEffect, useState, useRef, useCallback } from "react";

const videoConstraints = {
    width: 720,
    height: 360,
    facingMode: "user"
};

const ProgressBar = ({check}) => {
    const [style, setStyle] = useState({});

    setTimeout(() => {
        const newStyle = {
            width: "100%"
        }
        setStyle(newStyle);
    }, 100);

    console.log(check);
    return (
        <div>
            {check ? (<div className="text-slate-400">You can now upload this video</div>) : (<div className="text-slate-400">Record till the progress is complete</div>) }
            
            <div className="w-full bg-grey-300 h-3 mb-6 ">
                <div className="bg-red-400 h-3 rounded-lg w-0 transition-all duration-[9000ms]" style={style}></div>
            </div>
        </div>
    );
}



const Test = ({ childToParent }) => {
    const webcamRef = useRef(null);
    const mediaRecorderRef = useRef(null);
    const [capturing, setCapturing] = useState(false);
    const [recordedChunks, setRecordedChunks] = useState([]);
    const [progress, setProgress] = useState(false);
    const [completeVideo, setCompleteVideo] = useState(false);

    const handleStartCaptureClick = useCallback(() => {
        setProgress(true);
        setCapturing(true);

        setTimeout(() => {
            setCompleteVideo(true)
        },4000)
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
        <div>
            {progress ? (
                <ProgressBar check = {completeVideo} />
            ) : (
                <div className="flex flex-row space-x-1">
                    <div className="text-slate-400">To start press</div>
                    <div className="text-red-400">"Start Capture"</div>
                </div>
            )}
            <Webcam audio={false} ref={webcamRef} />
            {capturing ? (
                <button className="flex-1 btn bg-red-400 hover:bg-red-500 border-none" onClick={handleStopCaptureClick}>Stop Capture</button>
            ) : (
                <button className="flex-1 btn bg-red-400 hover:bg-red-500 border-none" onClick={handleStartCaptureClick}>Start Capture</button>
            )}
            {recordedChunks.length > 0 && (
                <button className="flex-1 btn bg-red-400 hover:bg-red-500 border-none" onClick={handleDownload}>Upload</button>
            )}
        </div>
    );
};

export default Test;