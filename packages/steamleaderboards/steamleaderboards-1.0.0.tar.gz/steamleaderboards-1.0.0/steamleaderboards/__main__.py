import argparse
import importlib.metadata
import pathlib
import sys
from . import LeaderboardGroup, ProtoLeaderboard, Leaderboard, Entry


parser = argparse.ArgumentParser(
	description="Retrieve scoreboards for a specific Steam game"
)

parser.add_argument("-o", "--output-dir", dest="output_dir", help="The directory where downloaded leaderboards should be stored in.", type=pathlib.Path)
parser.add_argument("app_id", type=int, nargs="+")
parser.add_argument("-V", "--version", action="version", version=importlib.metadata.version("steamleaderboards"))

def main():
	args = parser.parse_args()

	output_dir: pathlib.Path = (args.output_dir or pathlib.Path(".")).absolute()
	if output_dir.exists() and not output_dir.is_dir():
		print(f"error: output dir exists and is not a directory: {output_dir}", file=sys.stderr)
		exit(1)
	elif not output_dir.exists():
		print(f"created output directory: {output_dir}", file=sys.stderr)
		output_dir.mkdir(parents=True)
	else:
		print(f"using output directory: {output_dir}", file=sys.stderr)

	for app_id in args.app_id:
		print(f"fetching leaderboards for: {app_id}", file=sys.stderr)
		lg: LeaderboardGroup = LeaderboardGroup(app_id)
		for proto in lg.leaderboards:
			print(f"fetching full leaderboard: {app_id} {proto.name}", file=sys.stderr)
			full: Leaderboard = proto.full()
			with open(output_dir.joinpath(f"{full.app_id}_{full.name}.csv"), mode="w") as file:
				file.write(f"rank,steam_id,score,ugcid,details\n")
				for entry in full.entries:
					file.write(f"{entry.rank!r},{entry.steam_id!r},{entry.score!r},{entry.ugcid!r},{entry.details!r}\n")
		if len(lg.leaderboards) == 0:
			print(f"game has no leaderboards", file=sys.stderr)


if __name__ == "__main__":
	main()