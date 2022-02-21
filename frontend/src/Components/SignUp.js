const SignUp = () => {
	return (
		<div className="flex flex-col">
			<div className="flex place-content-center text-5xl my-5 text-blue-400">
				Thapar Attendence System
			</div>
			<div className="p-10 card bg-base-200 w-1/3 space-y-5 place-self-center">
				<div className="form-control">
					<label className="label">
						<span className="label-text">Username</span>
					</label>
					<input
						type="text"
						placeholder="Username"
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
						<span className="label-text">Contact</span>
					</label>
					<input
						type="text"
						placeholder="Contact"
						className="p-3 outline-none rounded-lg text-sm"
					/>
					<label className="label">
						<span className="label-text">Password</span>
					</label>
					<input
						type="password"
						placeholder="Password"
						className="p-3 outline-none rounded-lg text-sm"
					/>
				</div>
				<button class="btn w-1/3 bg-blue-400 hover:bg-blue-500 border-none">
					Sign in
				</button>
			</div>
		</div>
	);
};

export default SignUp;
