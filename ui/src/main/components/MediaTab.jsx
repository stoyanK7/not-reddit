import Image from "next/image";
import React, { useState } from "react";

export default function MediaTab({ setBody, success }) {
    const [selectedImage, setSelectedImage] = useState(null);
    return (
        <div>
            {selectedImage && (
                <div>
                    <Image
                        alt="Chosen image"
                        width={"400"}
                        height={"400"}
                        src={URL.createObjectURL(selectedImage)}
                    />
                    <br />
                    <button
                        className="py-2 px-4 rounded-sm bg-red-600 text-white w-full"
                        onClick={() => setSelectedImage(null)}>Remove
                    </button>
                </div>
            )}
            <input
                type="file"
                name="myImage"
                onChange={(event) => {
                    if (event.target.files) {
                        setSelectedImage(event.target.files[0]);
                        setBody(event.target.files[0]);
                    }
                }}
                disabled={success}
            />
        </div>
    );
}
