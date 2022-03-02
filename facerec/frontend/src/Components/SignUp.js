import { useState } from "react";
import axios from 'axios';

const SignUp = () => {
	axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
	axios.defaults.xsrfCookieName = "csrftoken";

	const [email, setEmail] = useState("");
	const [phone, setPhone] = useState(null);
	const [password, setPassword] = useState("");

	async function signIn() {
		let item = { email, phone, password };
		console.log(item);

		await axios({
			method: "post",
			// !!!!!!!! i have to change this to the api endpoint for signup which i have not got lol !!!!!!!!!!!!!!!!!!1
			url: "http://127.0.0.1:8080/auth/token/login",
			data: item,
		})
			.then((res) => console.log(res))
			.catch((err) => console.error(err))
	}

	return (
		<div className="flex flex-col">
			<div className="flex place-content-center text-5xl my-5 text-blue-400">
				Thapar Attendence System
			</div>
			<div className="p-10 card bg-base-200 w-1/3 space-y-5 place-self-center">
				<div className="form-control">
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
						<span className="label-text">Contact</span>
					</label>
					<input
						type="text"
						placeholder="Contact"
						className="p-3 outline-none rounded-lg text-sm"
						onChange={(e) => setPhone(e.target.value)}
					/>
					<label className="label">
						<span className="label-text">Password</span>
					</label>
					<input
						type="password"
						placeholder="Password"
						className="p-3 outline-none rounded-lg text-sm"
						onChange={(e) => setPassword(e.target.value)}
					/>
				</div>
				<button onClick={signIn} class="btn w-1/3 bg-blue-400 hover:bg-blue-500 border-none">
					Sign in
				</button>
			</div>
		</div>
	);
};

export default SignUp;
