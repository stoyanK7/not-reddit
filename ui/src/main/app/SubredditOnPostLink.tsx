import Link from 'next/link';
import Image from 'next/image';

export default function SubredditOnPostLink({ subreddit }: { subreddit: string }) {
    return (
        <div className="flex gap-2 items-center">
            <Link href={`r/${subreddit}`} passHref legacyBehavior>
                <a className="relative overflow-hidden w-6 h-6 rounded-full">
                    <Image
                        style={{ objectFit: 'contain' }}
                        alt={`${subreddit} logo`}
                        // TODO: Make request to get subreddit icon
                        // TODO: Default to something in case subreddit icon is not found
                        src="https://styles.redditmedia.com/t5_2qhx7/styles/communityIcon_ywbajib7a6m81.png"
                        fill />
                </a>
            </Link>
            <Link href={`r/${subreddit}`}>
                <span className="font-bold hover:underline hover:cursor-pointer">r/{subreddit}</span>
            </Link>
        </div>
    )
}
