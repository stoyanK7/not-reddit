import Image from "next/image";
import { loginRequest } from "@/app/authConfig";
import { useMsal } from "@azure/msal-react";

export default function IsNotSignedIn() {
    const { instance } = useMsal();

    return (
        <>
            <span>There are currently no users signed in!</span>
            <div className="relative overflow-visible w-1/2 h-10 hover:cursor-pointer">
                <Image
                    style={{ objectFit: 'contain' }}
                    alt="User avatar"
                    src="/ms-symbollockup-signin-light.svg"
                    fill
                    onClick={() => instance.loginRedirect(loginRequest)}
                    data-cy="signIn" />
            </div>
        </>
    )
}
