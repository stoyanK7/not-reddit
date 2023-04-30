import { toast } from "react-toast";

export default async function handleToast(res, successMessage) {
    if (res.ok) {
        toast.success(successMessage);
    } else {
        const data = await res.json();
        if (data.detail) {
            toast.error(data.detail);
        } else {
            toast.error("Something went wrong");
        }
    }
}
