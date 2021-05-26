from style_wraps import block, code_block
from services.HeroService import HeroService


def hero_commands(bot):
    @bot.group()
    async def hero(ctx):
        """Put this command to choose characteristics of your hero"""
        if not ctx.subcommand_passed:
            service = HeroService()
            try:
                sel_hero = service.get_selected_hero(ctx.author.id)
            except:
                await ctx.send(block('You don\'t have a hero yet.', ctx.author.id))
            else:
                await ctx.send(block(
                    '**Your hero**\nname: %s\nclass: %s' % (
                        sel_hero.name,
                        sel_hero.cls
                    ),
                    ctx.author.id
                ))

    @hero.command()
    async def name(ctx, _name: str):
        """To assign the name of your hero"""
        if _name:
            service = HeroService()
            service.assign_name(_name, ctx.author.id)
            await ctx.send(code_block('Your hero is now called %s!' % (_name,), mention_id=ctx.author.id))
        else:
            await ctx.send(code_block('You need to assign a name to your hero', mention_id=ctx.author.id))

    @hero.command()
    async def cls(ctx, _cls: str):
        """To assign the class of your hero"""
        await ctx.send(code_block('Your class is now %s!' % (_cls,), mention_id=ctx.author.id))
