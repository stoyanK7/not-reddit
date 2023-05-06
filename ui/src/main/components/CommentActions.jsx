import { toast } from "react-toast";

import buildAuthorizationHeader from "@/utils/buildAuthorizationHeader";
import buildJSONHeaders from "@/utils/buildJSONHeaders";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";
import handleToast from "@/utils/handleToast";

export default function CommentActions({ comment_id, votes, username, mutate }) {
    const isUserOwnerOfComment = username === sessionStorage.getItem("username");

    // TODO: Mimick that the user has already voted on the post
    async function upvote() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token");
            return;
        }

        const res = await fetch(fromApi("/api/vote/comment"), {
            method: "POST",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ "target_id": comment_id, "vote_type": "up" }),
        });

        await handleToast(res, "Upvoted comment successfully");
    }

    async function downvote() {
        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token");
            return;
        }

        const res = await fetch(fromApi("/api/vote/comment"), {
            method: "POST",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ "target_id": comment_id, "vote_type": "down" }),
        });

        await handleToast(res, "Downvoted comment successfully");
    }

    async function deleteComment(e) {
        e.preventDefault();
        e.stopPropagation();

        if (!isUserOwnerOfComment) {
            toast.error("You can only delete your own comments");
            return;
        }

        if (!confirm("Are you sure you want to delete this comment?")) {
            toast.info("Comment deletion cancelled");
            return;
        }

        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token");
            return;
        }

        const res = await fetch(fromApi(`/api/comment/${comment_id}`), {
            method: "DELETE",
            headers: buildAuthorizationHeader(accessToken)
        });

        mutate();
        await handleToast(res, `Comment with id ${comment_id} deleted successfully`);
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
            <div
                className="p-2 rounded-sm text-yellow-600 hover:bg-yellow-300">
                Award
            </div>
            {isUserOwnerOfComment &&
                <div
                    className="p-2 rounded-sm text-red-600 hover:bg-red-300"
                    onClick={deleteComment}>
                    Delete
                </div>
            }
        </div>
    );
}
