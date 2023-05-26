import Image from "next/image";
import Link from "next/link";

import AwardsBar from "@/components/AwardsBar";

export default function CommentInfo({ username, commentedAt, silverAwards, goldAwards,
    platinumAwards }) {
    return (
        <div
            className="flex gap-2">
            <a
                className="relative overflow-hidden w-6 h-6 rounded-full">
                <Image
                    style={{ objectFit: "contain" }}
                    alt="user logo"
                    src="/user-logo.png"
                    fill />
            </a>
            <Link
                href={`/user/${username}`}>
                u/{username}
            </Link>
            <span>•</span>
            {commentedAt &&
                <>
                    <span>on {commentedAt.split("T")[0]}</span>
                    <span>at {commentedAt.split("T")[1].slice(0,5)}</span>
                </>
            }
            <AwardsBar
                silverAwards={silverAwards}
                goldAwards={goldAwards}
                platinumAwards={platinumAwards} />
        </div>
    );
}
