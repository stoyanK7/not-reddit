import Link from "next/link";
import { useState } from "react";
import { toast } from "react-toast";

import buildAuthorizationHeader from "@/utils/buildAuthorizationHeader";
import buildJSONHeaders from "@/utils/buildJSONHeaders";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";
import getUsername from "@/utils/getUsername";
import handleToast from "@/utils/handleToast";

export default function PostActions({ id, votes, username, mutate }) {
    const [shownVotes, setShownVotes] = useState(votes);
    const isUserOwnerOfPost = username === getUsername();

    async function upvotePost(e) {
        e.preventDefault();
        e.stopPropagation();
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token");
            return;
        }

        const res = await fetch(fromApi("/api/vote/post"), {
            method: "POST",
            credentials: "include",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ "target_id": id, "vote_type": "up" }),
        });

        await handleToast(res, "Upvoted post successfully");

        if (res.ok) {
            setShownVotes(shownVotes + 1);
        }
    }

    async function downvotePost(e) {
        e.preventDefault();
        e.stopPropagation();
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token");
            return;
        }

        const res = await fetch(fromApi("/api/vote/post"), {
            method: "POST",
            credentials: "include",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ "target_id": id, "vote_type": "down" }),
        });

        await handleToast(res, "Downvoted post successfully");

        if (res.ok) {
            setShownVotes(shownVotes - 1);
        }
    }

    async function deletePost(e) {
        e.preventDefault();
        e.stopPropagation();

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
            credentials: "include",
            headers: buildAuthorizationHeader(accessToken)
        });

        mutate();
        await handleToast(res, `Post with id ${id} deleted successfully`);
    }

    async function sharePost(e) {
        e.preventDefault();
        e.stopPropagation();
        await navigator.clipboard.writeText(`${window.location.origin}/post/${id}`);
        toast.success("Copied post link to clipboard");
    }

    return (
        <div
            className="flex gap-2 text-reddit-gray hover:cursor-pointer">
            <div
                className="flex items-center">
                <button
                    className={`p-2 mr-1 rounded-sm hover:bg-reddit-orange-light text-reddit-orange
                    ${shownVotes > votes ? "bg-reddit-orange-light" : ""}`}
                    onClick={upvotePost}
                    disabled={shownVotes > votes}>
                    Up
                </button>
                <span
                    className="font-bold text-reddit-black">{shownVotes}</span>
                <button
                    className={`p-2 ml-1 rounded-sm hover:bg-reddit-blue-light text-reddit-blue
                    ${shownVotes < votes ? "bg-reddit-blue-light" : ""}`}
                    onClick={downvotePost}
                    disabled={shownVotes < votes}>
                    Down
                </button>
            </div>
            <Link
                href={`/post/${id}`}>
                <div
                    className="p-2 rounded-sm text-blue-600 hover:bg-blue-300">
                    Comments
                </div>
            </Link>
            <Link
                href={`/award?subject_id=${id}&subject_type=post`}>
                <div
                    className="p-2 rounded-sm text-yellow-600 hover:bg-yellow-300">
                    Award
                </div>
            </Link>
            <div
                onClick={sharePost}
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
