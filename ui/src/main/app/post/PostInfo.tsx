import Link from "next/link";
import PostSubreddit from "./PostSubreddit";

export default function PostInfo({
    subreddit = "all",
    username = "unknown",
    postedAt }
    : {
        subreddit: string,
        username: string,
        postedAt: string
    }
) {
    return (
        <div className="flex gap-2">
            <PostSubreddit subreddit={subreddit} />
            <span>•</span>
            <div className="flex gap-2">
                <span>
                    Posted by&nbsp;
                    <Link href={`/user/${username}`}>
                        u/{username}
                    </Link>
                </span>
                <span>{postedAt.split('T')[0]}</span>
            </div>
        </div>
    )
}
