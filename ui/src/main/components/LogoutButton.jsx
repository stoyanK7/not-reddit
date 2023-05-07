import { toast } from "react-toast";

import { msalInstance } from "@/utils/authConfig";

export default function LogoutButton() {
    async function logout() {
        await msalInstance.logoutPopup();
        toast.success("Logged out successfully.");
    }

    return (
        <button
            className="p-2 rounded-sm bg-red-800 text-white h-full"
            onClick={logout}
            data-cy="logOut">
            Logout
        </button>
    );
}
