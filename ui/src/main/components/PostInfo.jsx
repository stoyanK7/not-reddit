import Link from "next/link";

import PostSubreddit from "./PostSubreddit";

export default function PostInfo({
    subreddit = "all",
    username = "unknown",
    postedAt }
) {
    return (
        <div
            className="flex gap-2">
            <PostSubreddit
                subreddit={subreddit} />
            <span>•</span>
            <div
                className="flex gap-2">
                <span>
                    Posted by&nbsp;
                    <Link
                        href={`/user/${username}`}>
                        u/{username}
                    </Link>
                </span>
                <span>on {postedAt.split("T")[0]}</span>
                <span>at {postedAt.split("T")[1].slice(0,5)}</span>
            </div>
        </div>
    );
}
