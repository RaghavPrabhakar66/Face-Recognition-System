import Navbar from "./Navbar";
import { UserAddIcon } from "@heroicons/react/solid";
import { useState } from "react";
import { Listbox } from "@headlessui/react";
import UploadImages from "./UploadImages";

const people = [
    { id: 1, name: "Hostel A", unavailable: false },
    { id: 2, name: "Hostel B", unavailable: false },
    { id: 3, name: "Hostel C", unavailable: false },
    { id: 4, name: "Hostel D", unavailable: true },
    { id: 5, name: "Hostel H", unavailable: false },
    { id: 6, name: "Hostel I", unavailable: false },
    { id: 7, name: "Hostel J", unavailable: false },
    { id: 8, name: "Hostel K", unavailable: false },
    { id: 9, name: "Hostel L", unavailable: false },
    { id: 10, name: "Hostel M", unavailable: false },
];

const AddStudent = () => {
    const [selectedPerson, setSelectedPerson] = useState(people[0]);

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
                        />
                        <label className="label">
                            <span className="label-text">First Name</span>
                        </label>
                        <input
                            type="text"
                            placeholder="First Name"
                            className="p-3 outline-none rounded-lg text-sm"
                        />
                        <label className="label">
                            <span className="label-text">Last Name</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Last Name"
                            className="p-3 outline-none rounded-lg text-sm"
                        />
                        <label className="label">
                            <span className="label-text">Phone Number</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Phone Number"
                            className="p-3 outline-none rounded-lg text-sm"
                        />
                        <label className="label">
                            <span className="label-text">Email Id</span>
                        </label>
                        <input
                            type="text"
                            placeholder="Email Id"
                            className="p-3 outline-none rounded-lg text-sm"
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
                                {people.map((person) => (
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
                        <button className="btn w-1/3 bg-blue-400 hover:bg-blue-500 border-none ">
                            Submit
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
