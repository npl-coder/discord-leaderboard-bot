from random import choice
import discord
from sheet.sheet_operations import get_top_k_individual, get_top_k_place, add_new_user, increase_score


def get_help():
    embed = discord.Embed(
        title="Leaderboard Bot Help",
        description="List of available commands:",
        color=discord.Color.blue()
    )
    embed.add_field(name="npl top <k>",
                    value="Shows the top k users based on scores.", inline=False)
    embed.add_field(name="npl top_place <place> <k>",
                    value="Shows the top k places based on average scores.", inline=False)
    embed.add_field(name="npl add_user <name> <username> <province> <district> <school>",
                    value="[Admin Only] Adds a new user to the leaderboard with an initial score of 0.", inline=False)
    embed.add_field(name="npl increase_score <username> <points>",
                    value="[Admin Only] Increases the score of a user by the specified number of points.", inline=False)
    embed.set_footer(
        text="Use these commands to interact with the leaderboard!")
    return embed


def get_responses(user_input: str, is_admin: bool) -> str | discord.Embed:
    lowered: str = user_input.lower()
    
    if lowered == "":
        return "Well you're awfully silent..."
    elif lowered.startswith("npl "):
        # Remove the "npl " prefix
        command = lowered[4:]
        
        # Help command
        if command == "help":
            return get_help()
            
        # Top k users command
        elif command.startswith("top "):
            try:
                k = int(command.split()[1])
                if k <= 0:
                    return "Please provide a positive number for top k users"
                
                top_users = get_top_k_individual(k)
                if not top_users:
                    return "No users found in the leaderboard"
                
                embed = discord.Embed(
                    title=f"Top {k} Users",
                    description="Here are the top performers!",
                    color=discord.Color.gold()
                )
                
                for i, user in enumerate(top_users, 1):
                    try:
                        name = user.get('Name', 'Unknown')
                        username = user.get('Discord Username', 'Unknown')
                        score = user.get('Score', 0)
                        school = user.get('School', 'Unknown')
                        district = user.get('District', 'Unknown')
                        province = user.get('Province', 'Unknown')
                        
                        embed.add_field(
                            name=f"{i}. {name} ({username})",
                            value=f"Score: {score}\nSchool: {school}\nLocation: {district}, {province}",
                            inline=False
                        )
                    except Exception as e:
                        print(f"Error processing user {i}: {e}")
                        continue
                
                return embed
            except (IndexError, ValueError) as e:
                print(f"Error in top command: {e}")
                return "Please use the correct format: npl top <number>"
                
        # Top k places command
        elif command.startswith("top_place "):
            try:
                parts = command.split()
                place = parts[1]
                k = int(parts[2])
                
                if k <= 0:
                    return "Please provide a positive number for top k places"
                
                if place.lower() not in ['province', 'district', 'school']:
                    return "Place must be either 'province', 'district', or 'school'"
                
                top_places = get_top_k_place(place, k)
                if not top_places:
                    return f"No {place}s found in the leaderboard"
                
                embed = discord.Embed(
                    title=f"Top {k} {place.capitalize()}s",
                    description=f"Here are the top performing {place}s!",
                    color=discord.Color.green()
                )
                
                for i, place_data in enumerate(top_places, 1):
                    try:
                        place_name = place_data.get(place.capitalize(), 'Unknown')
                        avg_score = place_data.get('Average Score', 0)
                        
                        embed.add_field(
                            name=f"{i}. {place_name}",
                            value=f"Average Score: {avg_score:.2f}",
                            inline=False
                        )
                    except Exception as e:
                        print(f"Error processing place {i}: {e}")
                        continue
                
                return embed
            except (IndexError, ValueError) as e:
                print(f"Error in top_place command: {e}")
                return "Please use the correct format: npl top_place <province|district|school> <number>"
                
        # Add new user command
        elif command.startswith("add_user "):
            if not is_admin:
                return "❌ You need admin permissions to use this command!"
            try:
                _, name, username, province, district, school = command.split(" ", 5)
                add_new_user(name, username, province, district, school)
                return f"✅ Successfully added {name} ({username}) to the leaderboard!"
            except ValueError:
                return "Please use the correct format: npl add_user <name> <username> <province> <district> <school>"
                
        # Increase score command
        elif command.startswith("increase_score "):
            if not is_admin:
                return "❌ You need admin permissions to use this command!"
            try:
                _, username, points = command.split()
                points = int(points)
                increase_score(username, points)
                return f"✅ Successfully increased {username}'s score by {points} points!"
            except ValueError:
                return "Please use the correct format: npl increase_score <username> <points>"
        
        else:
            return "Unknown command. Use 'npl help' to see available commands."
            
    elif 'hello' in lowered:
        return 'hello there!'
    else:
        return choice(["I do not understand.", "What are you talking about?", "Do you mind rephrasing?"])
