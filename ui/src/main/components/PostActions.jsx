import Link from "next/link";
import { useRouter } from "next/router";
import { toast } from "react-toast";

import buildAuthorizationHeader from "@/utils/buildAuthorizationHeader";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";
import handleToast from "@/utils/handleToast";

export default function PostActions({ id, votes, username, mutate }) {
    const router = useRouter();

    function upvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }

    function downvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }

    async function deletePost() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token.");
            return;
        }

        const res = await fetch(fromApi(`/api/post/${id}`), {
            method: "DELETE",
            headers: buildAuthorizationHeader(accessToken)
        });

        mutate();
        await handleToast(res, "Post deleted successfully.");
    }

    return (
        <div
            className="flex gap-2 text-reddit-gray hover:cursor-pointer">
            <div
                className="flex items-center">
                <span
                    className="p-2 mr-1 rounded-sm hover:bg-reddit-gray-hover
                    hover:text-reddit-orange"
                    onClick={upvote}>
                    Up
                </span>
                <span
                    className="font-bold text-reddit-black">{votes}</span>
                <span
                    className="p-2 ml-1 rounded-sm hover:bg-reddit-gray-hover
                    hover:text-reddit-blue"
                    onClick={downvote}>
                    Down
                </span>
            </div>
            <Link
                href={`/post/${id}`}>
                <div
                    className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                    Comments
                </div>
            </Link>
            <div
                className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Award
            </div>
            <div
                className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Share
            </div>
            <div
                className="p-2 rounded-sm text-red-600 hover:bg-red-300"
                onClick={deletePost}>
                Delete
            </div>
        </div>
    );
}
