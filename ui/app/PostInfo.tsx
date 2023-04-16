import Link from "next/link";
import SubredditOnPostLink from "./SubredditOnPostLink";

export default function PostInfo({
    subreddit = "unknown",
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
            <SubredditOnPostLink subreddit={subreddit} />
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
