import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faLink, faImage } from "@fortawesome/free-solid-svg-icons";
import Link from "next/link";
import Image from "next/image";

export default function CreatePost() {
    return (
        <div className="flex items-center gap-2 text-reddit-gray bg-white rounded-md border
            border-[#cccccc] mb-4 p-2">
            <Link href="/r/subreddit" passHref legacyBehavior>
                <a className="relative w-10 h-10">
                    <Image
                        style={{ objectFit: 'contain' }}
                        alt="User avatar"
                        src="/redditor.png"
                        fill />
                </a>
            </Link>
            <input className="rounded-sm px-4 py-2 border-2 border-transparent bg-[#F6F7F8]
                hover:border-reddit-blue grow"
                type="text"
                placeholder="Create Post" />
            <Link href="" className="p-2 rounded-sm text-2xl hover:bg-reddit-gray-hover">
                <FontAwesomeIcon icon={faImage} />
            </Link>
            <Link href="" className="p-2 rounded-sm text-2xl hover:bg-reddit-gray-hover">
                <FontAwesomeIcon icon={faLink} />
            </Link>
        </div>
    )
}
