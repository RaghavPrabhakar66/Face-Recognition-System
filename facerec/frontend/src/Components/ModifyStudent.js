import Navbar from "./Navbar";
import { UserAddIcon } from "@heroicons/react/solid";
import { useEffect, useState } from "react";
import { Listbox } from "@headlessui/react";
import UploadImages from "./UploadImages";
import axios from "axios";

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
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";

    const [selectedPerson, setSelectedPerson] = useState(hostels[0]);
    const [rollno, setRollno] = useState(null);
    const [first_name, setFirstName] = useState("");
    const [last_name, setLastName] = useState("");
    const [phone, setPhone] = useState(null);
    const [email, setEmail] = useState("");
    const [hostel, setHostel] = useState("Hostel A");

    async function addStudent() {
        let item = { rollno, first_name, last_name, phone, email, hostel }
        console.log(item);

        await axios({
            method: "put",
            url: "http://127.0.0.1:8080/api/student-actions",
            data: item,
            headers: {
				Authorization : 'Token ' + localStorage.getItem("Token")
			}
        })
            .then((res) => console.log(res))
            .catch((err) => console.error(err))
    }

    useEffect(() => {
        setHostel(selectedPerson.name);
    }, [selectedPerson])

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
                            value={selectedPerson}
                            onChange={setSelectedPerson}
                        >
                            <Listbox.Button className="text-sm bg-white mb-2 p-3 rounded-lg">
                                {selectedPerson.name}
                            </Listbox.Button>
                            <Listbox.Options className="max-h-24 overflow-y-auto space-y-2 hover:cursor-pointer">
                                {hostels.map((person) => (
                                    <Listbox.Option
                                        key={person.id}
                                        value={person}
                                        disabled={person.unavailable}
                                        className="hover:bg-slate-200 rounded-lg transition-all duration-100 p-1 "
                                    >
                                        {person.name}
                                    </Listbox.Option>
                                ))}
                            </Listbox.Options>
                        </Listbox>
                    </div>
                    <div className="flex w-full justify-between ">
                        <button onClick={addStudent} className="btn w-1/3 bg-red-400 hover:bg-red-500 border-none ">
                            Modify Changes
                        </button>
                    </div>
                </div>
                <div className="divider divider-vertical"></div>
                <div className="flex flex-col space-y-2 w-1/2">
                    <div className="grid flex-grow card bg-base-200 rounded-box place-items-center">
                        content
                    </div>
                    <UploadImages />
                    {/* <div className="grid flex-grow card bg-base-200 rounded-box place-items-center">
						Upload Image
						<UploadImages />
					</div> */}
                </div>
            </div>
            {/* <div className="flex w-full bg-base-200 my-5 rounded-box h-full">
				Upload Images
			</div> */}
        </div>
    );
};

export default AddStudent;
