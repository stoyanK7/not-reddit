import Image from "next/image";
import Link from "next/link";

export default function PostSubreddit({ subreddit }) {
    return (
        <div
            className="flex gap-2 items-center">
            <Link
                href={`r/${subreddit}`} passHref legacyBehavior>
                <a
                    className="relative overflow-hidden w-6 h-6 rounded-full">
                    <Image
                        style={{ objectFit: "contain" }}
                        alt={`${subreddit} logo`}
                        src="/subreddit-logo.png"
                        fill />
                </a>
            </Link>
            <Link
                href={`r/${subreddit}`}>
                <span
                    className="font-bold hover:underline hover:cursor-pointer">r/{subreddit}</span>
            </Link>
        </div>
    );
}
