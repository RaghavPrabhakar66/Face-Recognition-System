import { useState, useRef, useEffect } from "react";

const UploadImages = () => {
	const [image, setImage] = useState(null); //contains the image dataurl
	const [preview, setPreview] = useState(null); //contains the actual image
	const fileInputRef = useRef(null); //used to handle change events of button and link to the input field
    const [gallery, setGallery] = useState([]);
	//comes into action whenever there is a change in the "image" state and invokes setPreview
	//FileReader is a default javascript function
	useEffect(() => {
		if (image) {
			const reader = new FileReader();
			reader.onloadend = () => {
				setPreview(reader.result);
			};
			reader.readAsDataURL(image);
		} else {
			setPreview(null);
		}
	}, [image]);

	return (
		<div className="grid flex-grow card bg-base-200 rounded-box place-items-center">
			{preview ? (
				<img
					src={preview}
					alt=""
					className=" m-3 max-h-48"
				/>
			) : (
				<div></div>
			)}
			<form className="flex absolute bottom-5 right-5">
				<input
					type="file"
					name="image"
					ref={fileInputRef}
					accept="image/*"
					className="hidden"
					onChange={(e) => {
						const file = e.target.files[0];
						if (file && file.type.substring(0, 5) === "image") {
							setImage(file);
						} else {
							setImage(null);
						}
					}}
				/>
				<button
					onClick={(e) => {
						e.preventDefault();
						fileInputRef.current.click();
					}}
					className="btn bg-red-400 hover:bg-red-500 border-none"
				>
					Upload Images
				</button>
			</form>
		</div>
	);
};

export default UploadImages;
