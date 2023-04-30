import Link from "next/link";
import { toast } from "react-toast";

import buildAuthorizationHeader from "@/utils/buildAuthorizationHeader";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";
import handleToast from "@/utils/handleToast";

export default function PostActions({ id, votes, username, mutate }) {
    const isUserOwnerOfPost = username === sessionStorage.getItem("username");

    function upvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }

    function downvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }

    async function deletePost() {
        if (!isUserOwnerOfPost) {
            toast.error("You can only delete your own posts");
            return;
        }

        if (!confirm("Are you sure you want to delete this post?")) {
            toast.info("Post deletion cancelled");
            return;
        }

        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token");
            return;
        }

        const res = await fetch(fromApi(`/api/post/${id}`), {
            method: "DELETE",
            headers: buildAuthorizationHeader(accessToken)
        });

        mutate();
        await handleToast(res, `Post with id ${id} deleted successfully`);
    }

    return (
        <div
            className="flex gap-2 text-reddit-gray hover:cursor-pointer">
            <div
                className="flex items-center">
                <span
                    className="p-2 mr-1 rounded-sm hover:bg-reddit-orange-light text-reddit-orange"
                    onClick={upvote}>
                    Up
                </span>
                <span
                    className="font-bold text-reddit-black">{votes}</span>
                <span
                    className="p-2 ml-1 rounded-sm hover:bg-reddit-blue-light text-reddit-blue"
                    onClick={downvote}>
                    Down
                </span>
            </div>
            <Link
                href={`/post/${id}`}>
                <div
                    className="p-2 rounded-sm text-blue-600 hover:bg-blue-300">
                    Comments
                </div>
            </Link>
            <div
                className="p-2 rounded-sm text-yellow-600 hover:bg-yellow-300">
                Award
            </div>
            <div
                className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Share
            </div>
            {isUserOwnerOfPost &&
                <div
                    className="p-2 rounded-sm text-red-600 hover:bg-red-300"
                    onClick={deletePost}>
                    Delete
                </div>
            }
        </div>
    );
}
