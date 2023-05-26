import Link from "next/link";

import AwardsBar from "@/components/AwardsBar";

import PostSubreddit from "./PostSubreddit";

export default function PostInfo({
    subreddit = "all",
    username = "unknown",
    postedAt,
    silverAwards,
    goldAwards,
    platinumAwards
}
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
            <AwardsBar
                silverAwards={silverAwards}
                goldAwards={goldAwards}
                platinumAwards={platinumAwards} />
        </div>
    );
}
