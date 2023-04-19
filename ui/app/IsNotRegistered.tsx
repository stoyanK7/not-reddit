import {useState} from "react";
import buildJSONHeaders from "@/app/buildJSONHeaders";
import getAccessToken from "@/app/getAccessToken";
import {useMsal} from "@azure/msal-react";
import {toast, ToastContainer} from "react-toast";

export default function IsNotRegistered() {
    const [username, setUsername] = useState("");
    const {instance, accounts} = useMsal();

    async function register() {
        const accessToken: string = await getAccessToken(instance, accounts);
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/user/`, {
            method: 'POST',
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({username, email: accounts[0].username}),
        });

        if (res.ok) {
            toast.success("Registered successfully.");
        }
    }

    return (
        <div className="p-4 flex flex-col gap-2 shadow-reddit border border-reddit-postline">
            <ToastContainer/>
            <span>
                It seems that you are not yet registered.
            </span>
            <span>
                Please select a username so we can finish your registration.
            </span>
            <input type="text"
                   className="border border-reddit-postline rounded-sm p-2"
                   placeholder="your-awesome-username"
                   onChange={e => setUsername(e.currentTarget.value)}/>
            <button className="p-2 rounded-sm bg-reddit-orange text-white"
                    onClick={register}>
                Register!
            </button>
        </div>
    );
}