import Navbar from "./Navbar";
import { useEffect, useState, useRef, useCallback } from "react";
import { Listbox } from "@headlessui/react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Webcam from "react-webcam";
import { CameraIcon, VideoCameraIcon } from '@heroicons/react/solid'
import Test from "./test";

const videoConstraints = {
    width: 720,
    height: 360,
    facingMode: "user"
};



const hostels = [
    { id: 1, name: "Hostel A", unavailable: false },
    { id: 2, name: "Hostel B", unavailable: false },
    { id: 3, name: "Hostel C", unavailable: false },
    { id: 4, name: "Hostel D", unavailable: false },
    { id: 5, name: "Hostel H", unavailable: false },
    { id: 6, name: "Hostel I", unavailable: false },
    { id: 7, name: "Hostel J", unavailable: false },
    { id: 8, name: "Hostel K", unavailable: false },
    { id: 9, name: "Hostel L", unavailable: false },
    { id: 10, name: "Hostel M", unavailable: false },
];

const AddStudent = () => {
    //webcam stuff
    const [isCaptureEnable, setCaptureEnable] = useState(false);
    const webcamRef = useRef(null);
    const [url, setUrl] = useState(null);
    const capture = useCallback(() => {
        const imageSrc = webcamRef.current?.getScreenshot();
        if (imageSrc) {
            setUrl(imageSrc);
        }
    }, [webcamRef]);
    

    //file input stuff
    const fileInputRef = useRef(null); //used to handle change events of button and link to the input field
    
    //csrf tokens
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";

    //student data
    const [selectedHostel, setSelectedHostel] = useState(hostels[0]);
    const [rollno, setRollno] = useState(null);
    const [first_name, setFirstName] = useState("");
    const [last_name, setLastName] = useState("");
    const [phone, setPhone] = useState(null);
    const [email, setEmail] = useState("");
    const [hostel, setHostel] = useState("Hostel A");
    const [videoRec, setVideoRec ] = useState(null); //set video parameters
    const navigate = useNavigate();

    const childToParent = (childdata) => {
        setVideoRec(childdata);
    }

    //axios request
    async function addStudent() {
        let formData = new FormData();
        formData.append('rollno', rollno);
        formData.append('first_name', first_name);
        formData.append('last_name', last_name);
        formData.append('phone', phone);
        formData.append('email', email);
        formData.append('hostel', hostel);
        formData.append('is_outside', false);
        console.log(videoRec);
        formData.append('video', videoRec);

        await axios({
            method: "post",
            url: "http://127.0.0.1:8080/api/students",
            data: formData,
            headers: {
                Authorization: 'Token ' + localStorage.getItem("Token"),
                'content-type': 'multipart/form-data'
            }
        })
            .then((res) => {
                console.log(res.data);
                if (res.data) {
                    navigate("/site/dashboard");
                } else {
                    alert("Invalid request")
                }
            })
            .catch((err) => console.error(err))
    }

    useEffect(()=> {
        if(videoRec){
            console.log(videoRec);
        }
    }, [videoRec])

    useEffect(() => {
        setHostel(selectedHostel.name);
    }, [selectedHostel])

    return (
        <div className="flex flex-col h-screen">
            <Navbar />
            <div className="flex flex-row w-full h-full">
                <div className="grid flex-grow p-10 card bg-base-200 space-y-5 h-full">
                    <div className="form-control">
                        <label className="label">
                            <span className="label-text">Roll Number</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Roll Number"
                            className="p-3 outline-none rounded-lg text-sm"
                            onChange={(e) => setRollno(e.target.value)}
                        />
                        <label className="label">
                            <span className="label-text">First Name</span>
                        </label>
                        <input
                            type="text"
                            placeholder="First Name"
                            className="p-3 outline-none rounded-lg text-sm"
                            onChange={(e) => setFirstName(e.target.value)}
                        />
                        <label className="label">
                            <span className="label-text">Last Name</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Last Name"
                            className="p-3 outline-none rounded-lg text-sm"
                            onChange={(e) => setLastName(e.target.value)}
                        />
                        <label className="label">
                            <span className="label-text">Phone Number</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Phone Number"
                            className="p-3 outline-none rounded-lg text-sm"
                            onChange={(e) => setPhone(e.target.value)}
                        />
                        <label className="label">
                            <span className="label-text">Email Id</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Email Id"
                            className="p-3 outline-none rounded-lg text-sm"
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <label className="label">
                            <span className="label-text">Hostel</span>
                        </label>
                        <Listbox
                            value={selectedHostel}
                            onChange={setSelectedHostel}
                        >
                            <Listbox.Button className="text-sm bg-white mb-2 p-3 rounded-lg">
                                {selectedHostel.name}
                            </Listbox.Button>
                            <Listbox.Options className="max-h-24 overflow-y-auto space-y-2 hover:cursor-pointer">
                                {hostels.map((hostel) => (
                                    <Listbox.Option
                                        key={hostel.id}
                                        value={hostel}
                                        disabled={hostel.unavailable}
                                        className="hover:bg-slate-200 rounded-lg transition-all duration-100 p-1 "
                                    >
                                        {hostel.name}
                                    </Listbox.Option>
                                ))}
                            </Listbox.Options>
                        </Listbox>
                    </div>
                    <div className="flex w-full justify-between ">
                        <button onClick={addStudent} className="btn w-1/3 bg-red-400 hover:bg-red-500 border-none ">
                            Add Student
                        </button>
                    </div>
                </div>
                <div className="divider divider-vertical"></div>
                <div className="flex flex-col space-y-2 w-1/2 ">
                    {/* !!!!!!!!!!!video camera!!!!!!!!!! */}
                    <div className="grid flex-grow bg-base-200 rounded-box place-items-center">
                        {isCaptureEnable && (
                            <div>
                                <Test childToParent={childToParent} />
                                <button className="btn bg-red-400 hover:bg-red-500 border-none" onClick={() => setCaptureEnable(false)}>Close</button>
                            </div>
                        )}
                    </div>
                    <div className="flex bg-blue-100 space-x-2">
                        {/* webcam upload option */}
                        <button
                            className="flex-1 btn bg-red-400 hover:bg-red-500 border-none"
                            onClick={() => setCaptureEnable(true)}>Upload from webcam <VideoCameraIcon className="ml-1 h-4 w-4" />
                        </button>
                        {/* ref for when the file is uploaded !! */}
                        <button onClick={(e) => {
                            e.preventDefault();
                            fileInputRef.current.click();
                        }}
                            className="flex-1 btn bg-red-400 hover:bg-red-500 border-none">
                            Upload Images <CameraIcon className="ml-1 h-4 w-4" />
                        </button>
                    </div>
                </div>
            </div>
        </div >
    );
};

export default AddStudent;
