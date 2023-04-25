import Image from "next/image";
import { loginRequest, msalInstance } from "@/app/authConfig";

export default function IsNotSignedIn() {
    return (
        <>
            <span data-cy="nobodySignedIn">There are currently no users signed in!</span>
            <div className="relative overflow-visible w-1/2 h-10 hover:cursor-pointer">
                <Image
                    style={{ objectFit: 'contain' }}
                    alt="User avatar"
                    src="/ms-symbollockup-signin-light.svg"
                    fill
                    onClick={() => msalInstance.loginRedirect(loginRequest)}
                    data-cy="signIn" />
            </div>
        </>
    )
}
