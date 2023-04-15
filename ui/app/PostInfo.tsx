import SubredditOnPostLink from "./SubredditOnPostLink";

export default function PostInfo() {
    return (
        <div className="flex gap-2">
            <SubredditOnPostLink />
            <span>•</span>
            <div>Posted by u/asdasd 1 day ago</div>
        </div>
    )
}
