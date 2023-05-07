import { useState } from "react";
import { toast } from "react-toast";

import buildJSONHeaders from "@/utils/buildJSONHeaders";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";
import handleToast from "@/utils/handleToast";


export default function CreateComment({ postId }) {
    const [commentBody, setCommentBody] = useState("");

    async function publishComment() {
        if (!commentBody) {
            toast.error("Comment cannot be empty");
            return;
        }

        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token.");
            return;
        }

        const res = await fetch(fromApi("/api/comment"), {
            method: "POST",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ "body": commentBody, "post_id": postId }),
        });

        await handleToast(res, "Comment created successfully");

        if (res.ok) {
            // TODO: There is probably a better way to push the new comment to the list
        }
    }

    return (
        <div
            className="flex flex-col gap-2">
            <span>Comment on the post</span>
            <textarea
                rows={10}
                onChange={e => setCommentBody(e.currentTarget.value)}
                placeholder="What are your thoughts?"
                className="bg-white px-4 py-2 rounded-sm border border-reddit-postline" />
            <button
                className="bg-reddit-orange p-2 rounded-sm text-white"
                onClick={publishComment}>Comment</button>
        </div>
    );
}
