import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
    faArrowUp,
    faArrowDown,
    faShare,
    faBookmark,
    faComment,
    faGift
} from "@fortawesome/free-solid-svg-icons";

export default function PostActions() {
    return (
        <div className="flex gap-2 text-not-reddit-grey hover:cursor-pointer">
            <div className="flex items-center">
                <FontAwesomeIcon icon={faArrowUp} className="mr-2 p-1 rounded-sm hover:bg-not-reddit-grey-hover hover:text-not-reddit-orange" />
                <span className="font-bold text-not-reddit-black">134</span>
                <FontAwesomeIcon icon={faArrowDown} className="ml-2 p-1 rounded-sm hover:bg-not-reddit-grey-hover hover:text-not-reddit-blue" />
            </div>
            <div className="p-2 rounded-sm hover:bg-not-reddit-grey-hover">
                <FontAwesomeIcon icon={faComment} className="mr-2" />
                Comments
            </div>
            <div className="p-2 rounded-sm hover:bg-not-reddit-grey-hover">
                <FontAwesomeIcon icon={faGift} className="mr-2" />
                Award
            </div>
            <div className="p-2 rounded-sm hover:bg-not-reddit-grey-hover">
                <FontAwesomeIcon icon={faShare} className="mr-2" />
                Share
            </div>
            <div className="p-2 rounded-sm hover:bg-not-reddit-grey-hover">
                <FontAwesomeIcon icon={faBookmark} className="mr-2" />
                Save
            </div>
        </div>
    )
}