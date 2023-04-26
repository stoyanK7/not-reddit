import { useMsal } from "@azure/msal-react";
import Link from "next/link";
import { toast } from "react-toast";
import { msalInstance } from "@/app/authConfig";

export default function IsSignedIn() {
    const { accounts } = useMsal();

    async function logout() {
        await msalInstance.logoutPopup();
        toast.success("Logged out successfully.");
    }

    return (
        <>
            <span>There are currently
                &nbsp;
                <b className="text-reddit-orange" data-cy="accountsAmount">
                    {accounts.length}
                </b>
                &nbsp;
                users signed in!
            </span>
            <Link href="/">
                <button className="p-2 rounded-sm bg-reddit-orange text-white">
                    Go to home page
                </button>
            </Link>
            <span>or..</span>
            <button className="p-2 rounded-sm bg-red-800 text-white"
                onClick={logout}
                data-cy="logOut">
                Logout
            </button>
        </>
    )
}