import Link from "next/link";
import { PublicationPage } from "@/components/publication-page";

export default function NotFound() {
  return (
    <PublicationPage eyebrow="404" title="Page not found" description="This benchmark page does not exist or is no longer published.">
      <p><Link className="action primary" href="/leaderboard">Open the leaderboard</Link></p>
    </PublicationPage>
  );
}
