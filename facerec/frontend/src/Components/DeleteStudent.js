import Navbar from "./Navbar";
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const DeleteStudent = () => {
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";

    const [id, setId] = useState(null);
    const navigate = useNavigate();

    async function deleteStudent() {
        let item = { id }
        console.log(item);

        await axios({
            method: "delete",
            url: "http://127.0.0.1:8080/api/student-actions/" + id,
            headers: {
				Authorization : 'Token ' + localStorage.getItem("Token")
			}
        })
            .then((res) => {
                console.log(res);
                if(res.status === 204)
                {
                    navigate("/site/dashboard");
                }
                else
                {
                    alert("Invalid ID\nPlease try again.");
                }
                
            })
            .catch((err) => console.error(err))
    }

    return (
        <div className="flex flex-col h-screen">
            <Navbar />
            <div className="flex flex-row w-full h-full">
                <div className="grid flex-grow p-10 card bg-base-200 space-y-5 h-full">
                    <div className="form-control">
                        <label className="label">
                            <span className="label-text">Student ID</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Student ID"
                            className="p-3 outline-none rounded-lg text-sm"
                            onChange={(e) => setId(e.target.value)}
                        />
                    </div>
                    <div className="flex w-full justify-between ">
                        <button onClick={deleteStudent} className="btn w-full bg-red-400 hover:bg-red-500 border-none ">
                            Delete Student
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default DeleteStudent;
