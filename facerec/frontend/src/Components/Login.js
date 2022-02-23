import { Link } from "react-router-dom";
import axios from 'axios';
import { useState } from "react";


const Login = () => {
	axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
	axios.defaults.xsrfCookieName = "csrftoken";

	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	async function login() {
		let item = { email, password };
		console.log(item);

		await axios({
			method: "post",
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
						<span className="label-text">Email</span>
					</label>
					<input
						type="text"
						placeholder="email"
						className="p-3 outline-none rounded-lg text-sm"
						onChange={(e) => setEmail(e.target.value)}
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
				<div className="flex justify-between">
					<Link to="/site/dashboard">
						<button onClick={login} class="btn bg-blue-400 hover:bg-blue-500 border-none">
							Log in
						</button></Link>
					<Link to="/site/signup">
						<div className="mt-3">Register now</div>
					</Link>
				</div>
			</div>
		</div>
	);
};

export default Login;
